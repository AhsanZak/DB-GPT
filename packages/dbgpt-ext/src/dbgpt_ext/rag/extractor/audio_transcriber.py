import os
import time
import whisper
from typing import Optional
from dbgpt.util.tracer import trace

class AudioTranscriber:
    """Audio transcription using Whisper"""
    
    def __init__(self, model_name: str = "base"):
        self.model_name = model_name
        self._model = None
    
    @property
    def model(self):
        if self._model is None:
            self._model = whisper.load_model(self.model_name)
        return self._model
    
    @trace()
    def transcribe_audio(self, audio_path: str, output_dir: Optional[str] = None) -> str:
        """
        Transcribe audio file to text
        
        Args:
            audio_path: Path to audio file (.mp3, .wav, .m4a, etc.)
            output_dir: Directory to save transcript (optional)
            
        Returns:
            str: Transcript text content
        """
        start_time = time.time()
        
        # Transcribe audio with Whisper
        whisper_result = self.model.transcribe(audio_path)
        transcript_text = str(whisper_result.get("text", "")).strip()
        
        # Optionally save transcript to file
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            audio_name = os.path.splitext(os.path.basename(audio_path))[0]
            txt_path = os.path.join(output_dir, f"{audio_name}_transcript.txt")
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(transcript_text)
        
        elapsed = time.time() - start_time
        print(f"Audio transcription completed in {elapsed:.2f}s")
        
        return transcript_text