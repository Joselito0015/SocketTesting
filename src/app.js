
const app = require('./index')
const port =3000



const httpserver = app.listen(port, ()=>{
    console.log('listening on port ' + port)
})

//Se crea las conexiones de socket.io para recibir una imagen y mandarla a todos los clientes conectados
const io = require('socket.io')(httpserver)
io.on('connection', (socket)=>{
    console.log('a user connected')
    socket.on('disconnect', ()=>{
        console.log('user disconnected')
    })

    socket.on('image', (msg)=>{
        console.log('image received')
        io.emit('image', msg)
    })
}
)

