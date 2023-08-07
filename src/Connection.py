import mysql.connector

def conectar():
    try:
        conn = mysql.connector.connect(
            user='root',
            password='nyanya117',
            host='localhost',
            database='mydb',
            port='3306'
        )
        print('Conexión exitosa')
        return conn
    except mysql.connector.Error as err:
        print(f'Error en la conexión: {err}')
        return None
    

    
def obtener_albumes(conn):
    try:
        cursor = conn.cursor()
        consulta = "SELECT idAlbum, nombre FROM Album"
        cursor.execute(consulta)
        albumes = cursor.fetchall()
        return albumes
    except mysql.connector.Error as e:
        print("Error al obtener los álbumes:", e)
        return None    

# ... Código de conexión y funciones existentes ...

def print_resultados(conn, telefono_cliente):
    try:
        if conn:
            cursor = conn.cursor()
            
            # Realizar la consulta y obtener los resultados
            consulta = """
                SELECT Cliente.nombre AS Nombre_Cliente, Cliente.telefono AS Telefono_Cliente, 
                       Album.nombre AS Album_Comprado, Grupo.nombre AS Grupo_Album,
                       FacturaAlbum.cantidad AS Cantidad_Albums,
                       Album.precio * FacturaAlbum.cantidad AS Total_Precio
                FROM Cliente
                INNER JOIN Factura ON Cliente.idCliente = Factura.Cliente_idCliente
                INNER JOIN FacturaAlbum ON Factura.idFactura = FacturaAlbum.Factura_idFactura
                INNER JOIN Album ON FacturaAlbum.Album_idAlbum = Album.idAlbum
                INNER JOIN Grupo ON Album.Grupo_idGrupo = Grupo.idGrupo;
            """
            cursor.execute(consulta)
            resultados = cursor.fetchall()
            cursor.close()
            
            return resultados
        else:
            print("No se pudo conectar a la base de datos")
            return None
    except mysql.connector.Error as e:
        print("Error en la consulta:", e)
        return None


def insertar_compra(conn, ventana):
    
    nombre_cliente = ventana.lineEdit_nom.text()
    direccion_cliente = ventana.lineEdit_dir.text()
    correo_cliente = ventana.lineEdit_correo.text()
    telefono_cliente = ventana.lineEdit_tel.text()  
    cantidad_compra = ventana.spinBoxCant.value()
    album_id = ventana.comboBoxDiscos.currentIndex() + 1
    
    datos_cliente = (nombre_cliente, direccion_cliente, correo_cliente, telefono_cliente)
    datos_compra = (cantidad_compra, album_id)
    
    try:
        cursor = conn.cursor()

        # Insertar datos del cliente en la tabla Cliente
        insert_cliente_query = "INSERT INTO Cliente (nombre, direccion, correo, telefono) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_cliente_query, datos_cliente)
        conn.commit()

        # Obtener el ID del cliente insertado
        cliente_id = cursor.lastrowid

        # Insertar una factura en la tabla Factura
        insert_factura_query = "INSERT INTO Factura (fecha, Cliente_idCliente) VALUES (NOW(), %s)"
        cursor.execute(insert_factura_query, (cliente_id,))
        conn.commit()

        # Obtener el ID de la factura insertada
        factura_id = cursor.lastrowid

        # Insertar datos de la compra en la tabla FacturaAlbum
        insert_compra_query = "INSERT INTO FacturaAlbum (cantidad, Factura_idFactura, Album_idAlbum) VALUES (%s, %s, %s)"
        print("hola?")
        cursor.execute(insert_compra_query, (datos_compra[0],factura_id,datos_compra[1]))
        conn.commit()
        

    except mysql.connector.Error as err:
        print(f"Error al insertar la compra: {err}")
    
    #finally:
    #   if 'cursor' in locals() and cursor.is_connected():
    #        cursor.close()

