import * as functions from 'firebase-functions';
import { onFlow } from '@genkit-ai/firebase/functions';
import { askSproutAgent } from './sprout_ai_agent';

// Deploy the askSproutAgent as a callable function
export const askSprout = onFlow(
  {
    name: 'askSproutAgent',
    httpMethod: 'POST',
    cors: true, // Enable CORS for web access
  },
  askSproutAgent
);

// This is the main Firebase Functions export
export * from './sprout_ai_agent';
