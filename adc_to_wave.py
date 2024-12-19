import wave

def adc_to_wav(adc_values, sample_rate, num_channels, bit_depth, output_file):
    """
    Converts ADC values to a WAV file.

    Parameters:
        adc_values (list or bytes): ADC raw data as a list of integers or byte string.
        sample_rate (int): Sampling rate (e.g., 44100 for 44.1 kHz).
        num_channels (int): Number of audio channels (1 for mono, 2 for stereo, etc.).
        bit_depth (int): Bit depth (e.g., 16 for 16-bit audio).
        output_file (str): Path to save the output WAV file.
    """
    byte_data = bytes(adc_values)

    num_frames = len(byte_data) // 128

    # Write to WAV file
    with wave.open(output_file, 'wb') as wav_file:
        wav_file.setnchannels(num_channels)
        wav_file.setsampwidth(1)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(byte_data)
    
    print(f"WAV file saved: {output_file}, Duration: {num_frames / sample_rate:.2f} seconds")

