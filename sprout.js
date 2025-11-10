// DOM Elements
const mainMenu = document.getElementById('main-menu');
const aiHelperUI = document.getElementById('ai-helper-ui');
const askButton = document.getElementById('ask-button');
const sparkyMascot = document.getElementById('sparky-mascot');
const statusMessage = document.getElementById('status-message');
const statusBody = document.getElementById('status-body');
const backButton = document.getElementById('back-btn');
const askBtn = document.getElementById('ask-btn');

// Check for browser support
if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
    statusMessage.textContent = "Sorry, your browser doesn't support speech recognition. Try Chrome or Edge.";
    askButton.disabled = true;
}

// Initialize Speech Recognition
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();
recognition.continuous = false;
recognition.interimResults = false;
recognition.lang = 'en-US';

// Initialize Speech Synthesis
const synth = window.speechSynthesis;

// Event Listeners
askBtn.addEventListener('click', () => {
    mainMenu.classList.add('hidden');
    aiHelperUI.classList.remove('hidden');});

backButton.addEventListener('click', () => {
    mainMenu.classList.remove('hidden');
    aiHelperUI.classList.add('hidden');
    // Stop any ongoing speech
    synth.cancel();
    if (recognition.running) {
        recognition.stop();
    }
});

askButton.addEventListener('click', startListening);

function startListening() {
    // Reset UI
    statusMessage.textContent = 'Listening...';
    statusBody.textContent = '';
    sparkyMascot.classList.add('listening');
    
    // Start speech recognition
    recognition.start();
    
    // Set a timeout to stop listening after 5 seconds of no speech
    setTimeout(() => {
        if (recognition.running) {
            recognition.stop();
            statusMessage.textContent = 'Time out. Try again!';
            sparkyMascot.classList.remove('listening');
        }
    }, 5000);
}

// Speech Recognition Handlers
recognition.onresult = async (event) => {
    const transcript = event.results[0][0].transcript;
    statusBody.textContent = `You asked: "${transcript}"`;
    statusMessage.textContent = 'Sparky is thinking...';
    
    try {
        // Call our Firebase Function
        const response = await callAiAgent(transcript);
        const answer = response.data.answer;
        
        // Display and speak the answer
        statusBody.textContent = answer;
        speakAnswer(answer);
    } catch (error) {
        console.error('Error calling AI agent:', error);
        statusMessage.textContent = 'Oops! Something went wrong. Please try again.';
        sparkyMascot.classList.remove('listening');
    }
};

recognition.onend = () => {
    sparkyMascot.classList.remove('listening');
};

recognition.onerror = (event) => {
    console.error('Speech recognition error', event.error);
    statusMessage.textContent = 'Error: ' + event.error;
    sparkyMascot.classList.remove('listening');
};

// Function to call the AI agent
async function callAiAgent(question) {
    // In a real implementation, this would call your Firebase Function
    // For now, we'll simulate a response
    return new Promise((resolve) => {
        // Simulate network delay
        setTimeout(() => {
            // This is a mock response - in the real app, this would be an actual API call
            const mockResponses = [
                "That's a great question! Let me think...",
                "Hmm, I know this one!",
                "I love talking about this!"
            ];
            const randomResponse = mockResponses[Math.floor(Math.random() * mockResponses.length)];
            
            resolve({
                data: {
                    answer: randomResponse
                }
            });
        }, 1500);
    });
    
    // In the real implementation, you would use something like:
    /*
    const functionUrl = 'https://your-firebase-project.cloudfunctions.net/askSproutAgent';
    const response = await fetch(functionUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question })
    });
    return await response.json();
    */
}

// Function to speak the answer
function speakAnswer(text) {
    // Cancel any ongoing speech
    synth.cancel();
    
    const utterance = new SpeechSynthesisUtterance(text);
    
    // Try to find a child-friendly voice
    const voices = synth.getVoices();
    const preferredVoices = ['Google UK English Female', 'Microsoft Zira Desktop', 'Samantha'];
    
    for (const voiceName of preferredVoices) {
        const voice = voices.find(v => v.name.includes(voiceName));
        if (voice) {
            utterance.voice = voice;
            break;
        }
    }
    
    // Set voice properties
    utterance.pitch = 1.2;  // Higher pitch for child-friendly voice
    utterance.rate = 0.9;   // Slightly slower for clarity
    
    // Update status when speech starts/ends
    utterance.onstart = () => {
        statusMessage.textContent = 'Sparky is speaking...';
    };
    
    utterance.onend = () => {
        statusMessage.textContent = 'Tap the button to ask another question!';
    };
    
    // Speak the text
    synth.speak(utterance);
}

// Load voices when they become available
if (speechSynthesis.onvoiceschanged !== undefined) {
    speechSynthesis.onvoiceschanged = () => {
        // This will ensure voices are loaded
    };
}
