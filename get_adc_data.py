import serial
import time

data_size = 128

def read_adc_from_serial(port, baud_rate, output_file, duration):
    """
    Reads ADC values from a serial port and saves them to a file.

    Parameters:
        port (str): Serial port (e.g., 'COM6').
        baud_rate (int): Baud rate (e.g., 9600).
        output_file (str): File to save the ADC values.
        duration (int): Time in seconds to read data.
    """
    try:
        # Open the serial port
        ser = serial.Serial(port, baud_rate, timeout=1)
        print(f"Connected to {port} at {baud_rate} baud.")
        
        # Open the output file
        with open(output_file, 'w') as file:
            start_time = time.time()
            print("Reading data...")
            
            while time.time() - start_time < duration:
                # Read a line from the serial port
                bytesData = ser.read(size=data_size)
                
                # Convert bytes to numbers
                data = [int(x) for x in bytesData]
                file.write(' '.join(map(str, data)) + '\n')
            
            print(f"Data saved to {output_file}.")
    
    except serial.SerialException as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nProcess interrupted.")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Serial port closed.")

