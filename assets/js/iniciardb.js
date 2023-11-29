// Utiliza o crea la base de datos "users"
use users

// Crea una colección llamada "alumnos" con el esquema especificado
db.createCollection("alumnos", {
validator: {
    $jsonSchema: {
    bsonType: "object",
    required: ["nombre", "apellido", "dni", "fechaAlta", "fechaModificacion"],
    properties: {
        id: {
        bsonType: "objectId",
        description: "ID único del alumno"
        },
        nombre: {
        bsonType: "string",
        description: "Nombre del alumno"
        },
        apellido: {
        bsonType: "string",
        description: "Apellido del alumno"
        },
        dni: {
        bsonType: "string",
        description: "DNI del alumno"
        },
        fechaAlta: {
        bsonType: "date",
        description: "Fecha de alta del alumno"
        },
        fechaModificacion: {
        bsonType: "date",
        description: "Fecha de modificación del alumno"
        },
        fechaBaja: {
        bsonType: "date",
        description: "Fecha de baja del alumno"
        }
    }
    }
}
});
