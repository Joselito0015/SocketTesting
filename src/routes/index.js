const HomeController = require('../home/controller.home')

const router = (app) => {
    app.use('/',HomeController)
}

module.exports = router