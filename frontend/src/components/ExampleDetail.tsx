import { useState } from 'react'
import { Example, ExecutionResult } from '../types'
import { runExample } from '../services/api'
import '../styles/ExampleDetail.css'

interface ExampleDetailProps {
  example: Example
  onBack: () => void
}

function ExampleDetail({ example, onBack }: ExampleDetailProps) {
  const [running, setRunning] = useState(false)
  const [output, setOutput] = useState<ExecutionResult | null>(null)
  const [error, setError] = useState<string | null>(null)

  const handleRun = async () => {
    try {
      setRunning(true)
      setError(null)
      const result = await runExample(example.id)
      setOutput(result)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to run example')
      console.error('Error running example:', err)
    } finally {
      setRunning(false)
    }
  }

  return (
    <div className="example-detail">
      <button className="back-button" onClick={onBack}>
        ← Back
      </button>
      
      <div className="detail-header">
        <h2>{example.name}</h2>
        <span className="category-badge">{example.category}</span>
      </div>

      <div className="detail-description">
        <p>{example.description}</p>
        <code className="file-path">{example.path}</code>
      </div>

      <div className="detail-actions">
        <button
          className="run-button"
          onClick={handleRun}
          disabled={running}
        >
          {running ? 'Running...' : 'Run Example'}
        </button>
      </div>

      {error && (
        <div className="detail-error">
          <h4>Error</h4>
          <p>{error}</p>
        </div>
      )}

      {output && (
        <div className="detail-output">
          <h4>Output</h4>
          {output.success ? (
            <div className="output-success">
              <p>Executed successfully!</p>
              {output.output && (
                <pre className="output-text">{output.output}</pre>
              )}
            </div>
          ) : (
            <div className="output-error">
              <p>Execution failed</p>
              {output.error && (
                <pre className="output-text">{output.error}</pre>
              )}
            </div>
          )}
        </div>
      )}
    </div>
  )
}

export default ExampleDetail
