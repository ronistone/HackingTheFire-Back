module.exports = function (application) {
    //POST
    application.post('/api/chamada', function(req, res){
        application.app.controllers.camada.salvarOcorrencia(application, req, res);
    });

    //GET
    application.get('/api/chamada', function(req, res){
        application.app.controllers.camada.getOcorrencias(application, req, res);
    });

    //GET BY ID
    application.get('/api/chamada/:id', function(req, res){
        application.app.controllers.camada.getOcorrenciaById(application, req, res);
    });

    //PUT
    application.put('/api/:id', function(req, res){
        application.app.controllers.camada.putOcorrencia(application, req, res);
    });
}
