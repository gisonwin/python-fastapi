import asyncio


async def handle_echo(reader, writer):
    data = await reader.read(1024)
    message = data.decode("utf-8")
    addr = writer.get_extra_info('peername')

    print(f'Received {message} from {addr}')

    print(f'Sending to {message}')

    writer.write(data)
    await writer.drain()

    print("Close the connection")
    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(handle_echo, '127.0.0.1', 8888)
    address = ','.join(str(sock.getsockname()) for sock in server.sockets)

    print(f'Serving on {address}')

    async with server:
        await server.serve_forever()


asyncio.run(main())
