import axios from 'axios'
import { Example, ExecutionResult } from '../types'

const API_BASE = '/api'

const api = axios.create({
  baseURL: API_BASE,
  timeout: 30000,
})

export const fetchExamples = async (): Promise<Example[]> => {
  const response = await api.get<Example[]>('/examples')
  return response.data
}

export const runExample = async (exampleId: string): Promise<ExecutionResult> => {
  const response = await api.post<ExecutionResult>(`/examples/${exampleId}/run`)
  return response.data
}

export const getExampleDetails = async (exampleId: string): Promise<Example> => {
  const response = await api.get<Example>(`/examples/${exampleId}`)
  return response.data
}
