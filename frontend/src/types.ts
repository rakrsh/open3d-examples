export interface Example {
  id: string
  name: string
  category: string
  description: string
  path: string
}

export interface ExecutionResult {
  success: boolean
  output: string
  error?: string
}
