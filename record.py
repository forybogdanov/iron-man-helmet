from get_adc_data import read_adc_from_serial
from adc_to_wave import adc_to_wav

# Example usage
port = 'COM6'  # Replace with your serial port
baud_rate = 9600
output_file = 'adc_values.txt'
duration = 5  # Duration in seconds to collect data

read_adc_from_serial(port, baud_rate, output_file, duration)


# Example usage
str = open('adc_values.txt', 'r').read()
filtered_str = str.replace('\n', '')
str_arr = str.split(' ')[:-1]
adc_values = []
for n in str_arr:
    try:
        num = int(n)
        adc_values.append(num)
    except ValueError as e:
        continue
# adc_values = [int(x) for x in str_arr]
sample_rate = 7000 # 7 kHz
num_channels = 1  # Mono
bit_depth = 16  # 16-bit audio
output_file = "output.wav"

adc_to_wav(adc_values, sample_rate, num_channels, bit_depth, output_file)
print(f"WAV file saved as {output_file}")