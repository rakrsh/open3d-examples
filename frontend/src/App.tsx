import { useState, useEffect } from 'react'
import './styles/App.css'
import Header from './components/Header'
import ExamplesList from './components/ExamplesList'
import ExampleDetail from './components/ExampleDetail'
import { Example } from './types'
import { fetchExamples } from './services/api'

function App() {
  const [examples, setExamples] = useState<Example[]>([])
  const [selectedExample, setSelectedExample] = useState<Example | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    loadExamples()
  }, [])

  const loadExamples = async () => {
    try {
      setLoading(true)
      setError(null)
      const data = await fetchExamples()
      setExamples(data)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load examples')
      console.error('Error loading examples:', err)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app">
      <Header />
      <main className="app-main">
        <div className="app-container">
          <ExamplesList 
            examples={examples} 
            selected={selectedExample}
            onSelect={setSelectedExample}
            loading={loading}
            error={error}
          />
          {selectedExample && (
            <ExampleDetail 
              example={selectedExample}
              onBack={() => setSelectedExample(null)}
            />
          )}
        </div>
      </main>
    </div>
  )
}

export default App
