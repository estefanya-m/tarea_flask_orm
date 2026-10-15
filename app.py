from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 1. Configuración de la aplicación (Estilo exacto de tu ingeniero)
app = Flask(__name__)
# Al usar sqlite:///almacen.db de esta forma, Flask creará automáticamente la carpeta 'instance'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///almacen.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 2. Definición del modelo Product
class Product(db.Model):
    __tablename__ = "products"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0, nullable=False)
    
    # Formato de impresión personalizado como el de tu ingeniero
    def __repr__(self):
        return f"Producto: {self.name}, Precio: {self.price}, Stock: {self.stock}"

# ---------------------------------------------------
# 3. Operaciones CRUD 
# ---------------------------------------------------

def init_db():
    with app.app_context():
        db.create_all()
        print("Base de datos y tablas creadas satisfactoriamente")

def insert_data():
    with app.app_context():
        prod1 = Product(name="Laptop Gamer", price=1200.50, stock=10)
        prod2 = Product(name="Mouse Óptico", price=25.00, stock=50)
        prod3 = Product(name="Teclado Mecánico", price=75.00) # stock por defecto 0
        
        db.session.add(prod1)
        db.session.add(prod2)
        db.session.add(prod3)
        db.session.commit()
        print("Productos insertados correctamente")

def query_data():
    with app.app_context():
        print("\nListado de productos disponibles")
        productos = Product.query.all()
        for item in productos:
            print(item)

def query_one():
    with app.app_context():
        print("\nObtener un solo registro (ID = 1)")
        producto = Product.query.filter_by(id=1).first()
        if producto:
            print(producto)
        else:
            print("Producto no encontrado")

def update_data():
    with app.app_context():
        print("\nActualización de un registro (ID = 2)")
        producto = Product.query.filter_by(id=2).first()
        if producto:
            producto.price = 30.00
            producto.stock = 45
            db.session.commit()
            print("Producto actualizado exitosamente")
        else:
            print("Producto no encontrado")

def delete_data():
    with app.app_context():
        print("\nEliminación de registros (ID = 3)")
        producto = Product.query.filter_by(id=3).first()
        if producto:
            db.session.delete(producto)
            db.session.commit()
            print("Producto eliminado satisfactoriamente")
        else:
            print("Producto no encontrado")

# 4. Flujo de ejecución del programa principal
if __name__ == "__main__":
    # Descomenta o comenta las funciones según lo que quieras probar o capturar
    init_db()
    insert_data()
    query_data()
    query_one()
    update_data()
    delete_data()
    
    print("\nListado final tras las operaciones CRUD")
    query_data()
