def transcription(seq):
    """DNA -> RNA Transcription. Timin yerine Urasil yazılır."""
    return seq.replace("T", "U")


print(transcription("GATGGAACTTGACTACGTAAATT"))


