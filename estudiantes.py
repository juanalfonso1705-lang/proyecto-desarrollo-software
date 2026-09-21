def mejor_estudiante(estudiantes):
    if not estudiantes:
        return None
    
    mejor = estudiantes[0]
    for estudiante in estudiantes:
        if estudiante["promedio"] > mejor["promedio"]:
            mejor = estudiante
    return mejor