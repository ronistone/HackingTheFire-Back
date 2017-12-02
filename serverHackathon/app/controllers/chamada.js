module.exports.salvarOcorrencia = function (application, req, res) {
    var connection = application.config.dbConnection;
    var Ocorrencia = new application.app.models.Ocorrencia(connection);

    Ocorrencia.salvarOcorrencia(req.body, res);
}

module.exports.getOcorrencias = function (application, req, res) {
    var connection = application.config.dbConnection;
    var Ocorrencia = new application.app.models.Ocorrencia(connection);

    Ocorrencia.getOcorrencias(application, req, res);
}

module.exports.getOcorrenciaById = function (application, req, res) {
    var connection = application.config.dbConnection;
    var Ocorrencia = new application.app.models.Ocorrencia(connection);

    Ocorrencia.getOcorrenciaById(application, req, res);
}

module.exports.putOcorrencia = function (application, req, res) {
    var connection = application.config.dbConnection;
    var Ocorrencia = new application.app.models.Ocorrencia(connection);

    Ocorrencia.putOcorrencia(application, req, res);
}

module.exports.deleteOcorrencia = function (application, req, res) {
    var connection = application.config.dbConnection;
    var Ocorrencia = new application.app.models.Ocorrencia(connection);

    Ocorrencia.deleteOcorrencia(application, req, res);
}
