from enocean_library.protocol.packet import Packet

# Read base id from EnOcean dongle and build a packet
packet_type = 0x01
data = [0xD2, 0x01, 1, 0x64, 0x00, 0x00, 0x00, 0x00, 0x00]
optional = []
packet = Packet(packet_type, data=data, optional=optional)
packet.build()  # This will create the byte representation of the packet
print("Packet built:", packet)