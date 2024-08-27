import pandas as pd


# fetch dataset
#adult = fetch_ucirepo(id=2)

# data (as pandas dataframes)
#X = adult.data.features
#y = adult.data.targets

# metadata
#print(adult.metadata)

# variable information
#print(adult.variables)

#x = adult

def datos():
    from ucimlrepo import fetch_ucirepo

    url = url = 'https://archive.ics.uci.edu/static/public/2/data.csv'

    df = pd.read_csv(url)

    # 1. Número de personas de cada raza
    race_count = df['race'].value_counts()

    # 2. Edad promedio de los hombres
    edad_prom = df[df['sex'] == 'Male']['age'].mean()
    edad_prom = int(edad_prom)

    # 3. Porcentaje de personas con licenciatura
    porcentage_licenciatura = (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100
    porcentage_licenciatura = "{:.2f}%".format(porcentage_licenciatura)

    # 4. Porcentaje de personas con educación avanzada que ganan >50K
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = (higher_education[higher_education['income'] == '>50K'].shape[0] / higher_education.shape[0]) * 100
    salario_mayor_a_50k = "{:.2f}%".format(higher_education_rich)

    # 5. Porcentaje de personas sin educación avanzada que ganan >50K
    sin_educacion_avanzada = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    sin_educacion_avanzada_rich = (sin_educacion_avanzada[sin_educacion_avanzada['income'] == '>50K'].shape[0] / sin_educacion_avanzada.shape[0]) * 100
    sin_educacion_avanzada_rich = "{:.2f}%".format(sin_educacion_avanzada_rich)

    # 6. Número mínimo de horas trabajadas por semana
    num_horas_semana = df['hours-per-week'].min()


    # 7. Porcentaje de personas que trabajan el mínimo de horas y ganan >50K
    num_horas_minimas = df[df['hours-per-week'] == num_horas_semana]
    porcentaje_num_horas_minimas = (num_horas_minimas[num_horas_minimas['income'] == '>50K'].shape[0] / num_horas_minimas.shape[0]) * 100
    porcentaje_num_horas_minimas = "{:.2f}%".format(porcentaje_num_horas_minimas)

    # 8. País con el mayor porcentaje de personas que ganan >50K
    paises_porcentaje = df[df['income'] == '>50K']['native-country'].value_counts() / df[
    'native-country'].value_counts() * 100
    pais_mayor_porcentaje = paises_porcentaje.idxmax()
    porcentaje_mayor = paises_porcentaje.max()
    porcentaje_mayor = "{:.2f}%".format(porcentaje_mayor)

    # 9. Ocupación más popular para quienes ganan >50K en la India
    ocupacion_popular = df[(df['native-country'] == 'India') & (df['income'] == '>50K')]['occupation'].value_counts().idxmax()


    calculations = {
        'raza': race_count,
        'edad_promedio': edad_prom,
        'porcentaje de licenciatuta': porcentage_licenciatura,
        'educacion avanzada': salario_mayor_a_50k,
        'sin educacion avanzada': sin_educacion_avanzada_rich,
        'numero minimo de horas Trab': num_horas_semana,
        'minimo de horas, salario > 50':porcentaje_num_horas_minimas,
        'pais con el mayor porcentaje con personas que ganan mas de 50': pais_mayor_porcentaje,
        'el porcentaje del pais con mayor numero de personas que ganan mas de 50': porcentaje_mayor,
        'ocupacion mas popular en India': ocupacion_popular


    }

    return calculations