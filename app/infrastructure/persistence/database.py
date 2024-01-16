import json
from app import app, db
from app.core.use_cases.vulnerability import Vulnerability



def save_to_database(json_file_path):
    with app.app_context():
        with open(json_file_path, 'r') as json_file:
            reporte = json.load(json_file)

        try:
            new_vulnerability = Vulnerability(
                title="Información general",
                description=json.dumps(reporte)
            )

            db.session.add(new_vulnerability)
            db.session.commit()

            # Guardar las vulnerabilidades
            for vulnerability in reporte.get("vulnerabilities", []):
                new_vulnerability = Vulnerability(
                    title=vulnerability.get("title", ""),
                    description=vulnerability.get("description", "")
                )

                db.session.add(new_vulnerability)
                db.session.commit()

            print("JSON guardado en la base de datos.")
        except Exception as e:
            print(f"Error al guardar en la base de datos: {e}")
            print(f"JSON no procesado: {reporte}")
            db.session.rollback()
        finally:
            db.session.close()