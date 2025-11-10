import { defineFlow, runFlow } from '@genkit-ai/core';
import { retrieve } from '@genkit-ai/retriever';
import { googleAI } from '@genkit-ai/vertexai';
import * as fs from 'fs';
import * as path from 'path';

// Initialize Google AI plugin
const geminiPro = googleAI('gemini-pro');

// Simple text file retriever
async function simpleRetriever(query: string) {
  const contentDir = path.join(__dirname, '../content');
  const files = fs.readdirSync(contentDir).filter(file => file.endsWith('.txt'));
  
  let allContent = '';
  
  for (const file of files) {
    const content = fs.readFileSync(path.join(contentDir, file), 'utf-8');
    allContent += `\n\n--- ${file} ---\n${content}`;
  }
  
  // Simple keyword matching for retrieval
  const queryTerms = query.toLowerCase().split(/\s+/);
  const score = queryTerms.reduce((score, term) => {
    return score + (allContent.toLowerCase().includes(term) ? 1 : 0);
  }, 0);
  
  return [{
    content: allContent,
    metadata: { source: 'content_files' },
    score: score / Math.max(1, queryTerms.length) // Normalize score
  }];
}

// Define the main flow
export const askSproutAgent = defineFlow(
  {
    name: 'askSproutAgent',
    inputSchema: {
      type: 'object',
      properties: {
        question: { type: 'string' },
      },
      required: ['question'],
    },
    outputSchema: {
      type: 'object',
      properties: {
        answer: { type: 'string' },
      },
      required: ['answer'],
    },
  },
  async ({ question }) => {
    // Retrieve relevant context
    const retrievalResults = await retrieve({
      query: question,
      retriever: simpleRetriever,
      options: { k: 3 },
    });
    
    // Extract the content from retrieval results
    const context = retrievalResults
      .map(r => r.content)
      .join('\n\n')
      .substring(0, 2000); // Limit context length

    // System prompt to guide the AI's response
    const systemPrompt = `You are 'Sparky', a happy, friendly robot talking to a 3-5 year old child. 
    Your goal is to answer their questions in a simple, cheerful, and engaging way. 
    Use the provided context to answer their question. 
    Keep your answer to ONE simple, cheerful sentence. 
    Use simple words and concepts that a young child can understand. 
    Be warm, encouraging, and fun!`;

    // Generate the response using Gemini
    const prompt = `Context for answering the question:
${context}

Question: ${question}

Answer in a very simple, friendly way for a young child:`;

    const response = await geminiPro.generate({
      prompt: {
        text: prompt,
        system: systemPrompt,
      },
      config: {
        temperature: 0.7,
        maxOutputTokens: 100,
        topP: 0.9,
        topK: 40,
      },
    });

    // Extract the generated text
    const answer = response.text() || "Hmm, I'm not sure about that. Let's ask something else!";
    
    return {
      answer: answer,
    };
  }
);

// For local testing
if (require.main === module) {
  (async () => {
    const result = await runFlow(askSproutAgent, {
      question: "Why is the sky blue?",
    });
    console.log('Answer:', result.answer);
  })();
}
