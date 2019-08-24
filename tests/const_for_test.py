from citizens_api.const import CITIZENS, CITIZEN_ID, TOWN, STREET, BUILDING, APARTMENT, NAME, BIRTH_DATE, GENDER, \
    RELATIVES

BASE_IMPORT = {
    CITIZENS: [
        {
            CITIZEN_ID: 1,
            TOWN: "Москва",
            STREET: "Льва Толстого",
            BUILDING: "16к7стр5",
            APARTMENT: 7,
            NAME: "Иванов Иван Иванович",
            BIRTH_DATE: "26.12.1986",
            GENDER: "male",
            RELATIVES: [2]
        },
        {
            CITIZEN_ID: 2,
            TOWN: "Москва",
            STREET: "Льва Толстого",
            BUILDING: "16к7стр5",
            APARTMENT: 7,
            NAME: "Иванов Сергей Иванович",
            BIRTH_DATE: "17.04.1997",
            GENDER: "male",
            RELATIVES: [1]
        },
        {
            CITIZEN_ID: 3,
            TOWN: "Керчь",
            STREET: "Иосифа Бродского",
            BUILDING: "2",
            APARTMENT: 11,
            NAME: "Романова Мария Леонидовна",
            BIRTH_DATE: "23.11.1986",
            GENDER: "female",
            RELATIVES: []
        }
    ]
}

PATCH_DICT = {
    TOWN: "Москва",
    STREET: "Льва Толстого",
    BUILDING: "16к7стр5",
    APARTMENT: 7,
    NAME: "Иванова Мария Леонидовна",
    BIRTH_DATE: "26.12.1986",
    GENDER: "male",
    RELATIVES: [1]
}

CORRUPTIONS = {
    CITIZEN_ID: (None, "", "&", 2),
    TOWN: (None, "", "&", 2),
    STREET: (None, "", "&", 2),
    BUILDING: (None, "", "&", 2),
    APARTMENT: (None, "", "&", 1.456),
    NAME: (None, "", 2),
    BIRTH_DATE: (None, "", "&", "31.02.2019", "12.28.2019", "31.12.19", "31/12/2019", "2019.12.31"),
    GENDER: (None, "", "&", 1, "agender"),
    RELATIVES: (None, "", "&", [3], [2, 2])
}
