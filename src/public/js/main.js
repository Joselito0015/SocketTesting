//Crear una conexión para recibir una imagen por socket.io y renderizarla en el cliente
const socket = io()
socket.on('image', (msg)=>{
    console.log('image received')
    const image = document.getElementById('image')
    image.src = msg

})

