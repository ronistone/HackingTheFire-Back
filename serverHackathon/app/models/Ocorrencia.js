var objectId = require('mongodb').ObjectId;

function Ocorrencia(connection){
    this._connection = connection();
}

Ocorrencia.prototype.salvarOcorrencia = function (ocorrencia) {
    this._connection.open( function(err, mongoclient){
        mongoclient.collection('ocorrencias', function(err, collection){
            collection.insert(ocorrencia);
            mongoclient.close();
        });
    });
}

Ocorrencia.prototype.getOcorrencias = function(application, req, res){
    this._connection.open( function(err, mongoclient){
        mongoclient.collection('ocorrencias', function(err, collection){
            collection.find().toArray(function(err, results){
                if(err){
                    res.json(err);
                } else {
                    res.json(results);
                }
                mongoclient.close();
            });
        });
    });
}

Ocorrencia.prototype.getOcorrenciaById = function(application, req, res){
    this._connection.open( function(err, mongoclient){
        mongoclient.collection('ocorrencias', function(err, collection){
            collection.find(objectId(req.params.id))
                .toArray(function (err, result) {
                    res.json(result);
                });
            mongoclient.close();
        });
    });
}

/*
Ocorrencia.prototype.putOcorrencias = function(application, req, res){
    this._connection.open( function(err, mongoclient){
        mongoclient.collection('ocorrencias', function(err, collection){
            collection.find().toArray(function(err, results){
                if(err){
                    res.json(err);
                } else {
                    res.json(results);
                }
                mongoclient.close();
            });
        });
    });
}*/

module.exports = function () {
    return Ocorrencia;
}
