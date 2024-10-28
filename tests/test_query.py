import sqlite3
import pytest

from database.query import *


# # Test para obtener los datos de maestros por apellido
def test_get_maestros_data_by_apellido():
    conn = sqlite3.connect("instance/easyGrade.db")

    df = get_maestros_data_by_apellido(
        conn, "Rodriguez"
    )  # Obtener los datos del maestro

    assert len(df) == 1
    nombre = df["NOMBRE"].values[
        0
    ]  # Obtener nombre del primer maestro en el Data Frame
    assert isinstance(nombre, str)  # Verificar que el "nombre" sea string
    assert nombre == "Marta"


# Test para obtener datos de alumnos por ID de materia
def test_get_alumnos_data_by_materia_id():
    conn = sqlite3.connect("instance/easyGrade.db")

    df = get_alumnos_data_by_materia_id(conn, 1)

    assert not df.empty
    alumno_materia = df["MATERIA_ID"].values[0]
    assert isinstance(int(alumno_materia), int)
    assert alumno_materia == 1


# Test para obtener datos de maestros por ID de materia
def test_get_maestros_by_materia_id():
    conn = sqlite3.connect("instance/easyGrade.db")
    df = get_maestros_by_materia_id(conn, 1)

    assert not df.empty
    nombre = df["NOMBRE"].values[0]
    assert isinstance(nombre, str)
    assert nombre == "Marta"


# Test para obtener el promedio de calificaciones por ID de alumno
def test_get_average_calificacion_by_alumno_id():
    conn = sqlite3.connect("instance/easyGrade.db")
    promedio = get_average_calificacion_by_alumno_id(conn, 1)

    assert promedio is not None
    assert isinstance(promedio, (int, float))
    assert promedio == 9.0


# Test para obtener materias por ID de maestro
def test_get_materias_by_maestro_id():
    conn = sqlite3.connect("instance/easyGrade.db")
    df = get_materias_by_maestro_id(conn, 1)

    assert not df.empty
    materia = df["NOMBRE"].values[0]
    assert isinstance(materia, str)
    assert materia == "Matematicas"


# Test para contar alumnos por ID de maestro
def test_count_alumnos_by_maestro_id():
    conn = sqlite3.connect("instance/easyGrade.db")
    count = count_alumnos_by_maestro_id(conn, 1)

    assert isinstance(count, int)
    assert count >= 0


# Test para obtener las tareas por ID de alumno
def test_get_tareas_by_alumno_id():
    conn = sqlite3.connect("instance/easyGrade.db")
    df = get_tareas_by_alumno_id(conn, 1)

    assert not df.empty
    assert "ALUMNO_ID" in df.columns
    assert "DESCRIPCION" in df.columns

    tareas = df["DESCRIPCION"].tolist()
    assert isinstance(tareas, list), "Tareas should be a list."

    assert tareas == [
        "Problema 1",
        "Problema 2",
        "Problema 3",
    ]


# Test para obtener alumnos por materia, ordenados por apellido y nombre
def test_get_alumnos_by_materia_ordered_by_apellido_nombre():
    conn = sqlite3.connect("instance/easyGrade.db")
    df = get_alumnos_by_materia_ordered_by_apellido_nombre(conn, 1)

    assert not df.empty
    alumno = f"{df['NOMBRE'].values[0]} {df['APELLIDO'].values[0]}"
    assert isinstance(alumno, str)
    assert alumno == "Juan Perez"
