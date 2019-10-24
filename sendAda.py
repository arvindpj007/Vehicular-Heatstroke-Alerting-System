# Import library and create instance of REST client.
from Adafruit_IO import Client
aio = Client('arvindpj007', '3cf5f1a58a2a4d75bd5f430356d35106')

# Send the value 100 to a feed called 'Foo'.
aio.send('faces', 100)

# Retrieve the most recent value from the feed 'Foo'.
# Access the value by reading the `value` property on the returned Data object.
# Note that all values retrieved from IO are strings so you might need to convert
# them to an int or numeric type if you expect a number.
data = aio.receive('faces')
print('Received value: {0}'.format(data.value))