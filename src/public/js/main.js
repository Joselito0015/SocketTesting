//Crear una conexión para recibir una imagen por socket.io y renderizarla en el cliente
const socket = io()

socket.on('image', image => {
    console.log("Image received from server");
    let img = document.getElementById('image');
    img.src = `data:image/jpeg;base64,${image}`;
  });