import { Example } from '../types'
import '../styles/ExamplesList.css'

interface ExamplesListProps {
  examples: Example[]
  selected: Example | null
  onSelect: (example: Example) => void
  loading: boolean
  error: string | null
}

function ExamplesList({ examples, selected, onSelect, loading, error }: ExamplesListProps) {
  if (loading) {
    return <div className="examples-list loading">Loading examples...</div>
  }

  if (error) {
    return <div className="examples-list error">Error: {error}</div>
  }

  // Group examples by category
  const grouped = examples.reduce((acc, example) => {
    if (!acc[example.category]) {
      acc[example.category] = []
    }
    acc[example.category].push(example)
    return acc
  }, {} as Record<string, Example[]>)

  return (
    <div className="examples-list">
      <div className="examples-header">
        <h2>Examples</h2>
        <p className="examples-count">{examples.length} available</p>
      </div>
      
      <div className="examples-content">
        {Object.entries(grouped).map(([category, items]) => (
          <div key={category} className="category-section">
            <h3 className="category-title">{category}</h3>
            <ul className="examples-items">
              {items.map((example) => (
                <li key={example.id}>
                  <button
                    className={`example-item ${selected?.id === example.id ? 'active' : ''}`}
                    onClick={() => onSelect(example)}
                  >
                    <span className="example-name">{example.name}</span>
                    <span className="example-description">{example.description}</span>
                  </button>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  )
}

export default ExamplesList
