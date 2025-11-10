# SparkleSprout 🌟

A voice-first e-learning web application designed for children aged 2-5 years old. SparkleSprout features a friendly AI assistant named Sparky that answers children's questions using safe, pre-approved content through a Genkit RAG (Retrieval-Augmented Generation) system.

## Features

- 🎤 Voice-based interaction using the Web Speech API
- 🤖 Child-friendly AI responses with the Gemini model
- 🎨 Kid-friendly, accessible UI with large buttons and simple navigation
- 🔍 Context-aware responses using RAG (Retrieval-Augmented Generation)
- 📱 Responsive design that works on tablets and desktops

## Prerequisites

- Node.js 18 or higher
- npm (comes with Node.js)
- Firebase CLI (`npm install -g firebase-tools`)
- A Google account (for Firebase)
- A Google Cloud Project with the Vertex AI API enabled

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/sparkle-sprout.git
cd sparkle-sprout
```

### 2. Set Up Firebase

1. Log in to Firebase:
   ```bash
   firebase login
   ```

2. Initialize Firebase in your project:
   ```bash
   firebase init
   ```
   - Select both `Functions` and `Hosting`
   - Choose your Firebase project or create a new one
   - For functions, choose TypeScript
   - For hosting, set the public directory to `public`
   - Configure as a single-page app: `Yes`
   - Set up automatic builds: `No`

### 3. Install Dependencies

```bash
# Install frontend dependencies (from project root)
npm install

# Install Firebase Functions dependencies
cd functions
npm install
cd ..
```

### 4. Set Up Environment Variables

1. Create a `.env` file in the `functions` directory:
   ```
   GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-key.json"
   GCP_PROJECT_ID="your-gcp-project-id"
   ```

2. Make sure to add `.env` to your `.gitignore` file.

### 5. Deploy the Application

```bash
# Build and deploy Firebase Functions and Hosting
firebase deploy
```

### 6. Local Development

To run the application locally:

```bash
# Start the Firebase emulator
firebase emulators:start

# In a separate terminal, navigate to the public directory and serve the frontend
cd public
npx serve
```

Visit `http://localhost:5000` to access the application.

## Project Structure

```
/sparkle-sprout
  ├── /public               # Frontend files (HTML, CSS, JS)
  │   ├── index.html        # Main HTML file
  │   ├── sprout.css        # Styles
  │   └── sprout.js         # Frontend JavaScript
  │
  └── /functions            # Firebase Functions
      ├── /src
      │   ├── index.ts      # Firebase Functions entry point
      │   └── sprout_ai_agent.ts  # AI agent implementation
      ├── /content          # Content for RAG
      │   ├── story_dragon.txt
      │   └── fact_sky.txt
      └── package.json      # Dependencies
```

## Adding Content

To add more content for the AI to reference:

1. Add `.txt` files to the `functions/content/` directory
2. The AI will automatically include this content in its knowledge base
3. Files should contain simple, child-friendly text

## Customization

### Styling

- Colors and styling can be modified in `public/sprout.css`
- Update the color scheme in the `:root` variables at the top of the file

### AI Behavior

- Adjust the system prompt in `functions/src/sprout_ai_agent.ts` to change how Sparky responds
- Modify the temperature and other parameters to adjust response creativity

## Security Considerations

- The app is designed to be safe for children with content filtering
- All AI responses are based on the provided content files
- No personal data is collected or stored

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Firebase](https://firebase.google.com/)
- Powered by [Google's Gemini](https://ai.google/discover/gemini/)
- Icons from [Font Awesome](https://fontawesome.com/)
- Fonts from [Google Fonts](https://fonts.google.com/)
