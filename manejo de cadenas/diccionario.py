
empleado ={
    123: {"nombre": "david",
          "cargo": "panadero",
          "tipo_doc": "ce"
    },
    456:{
        "nombre": "ricardo",
         "cargo": "code",
          "tipo_doc": "cc"
    }
}

print(empleado.get(456,"no disponible")["tipo_doc"])
