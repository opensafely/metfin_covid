from ehrql.tables.tpp import (
    patients, 
    practice_registrations, 
    addresses, 
    appointments, 
    occupation_on_covid_vaccine_record,
    vaccinations,
    sgss_covid_all_tests,
    apcs, 
    ec, 
    opa, 
    opa_diag, 
    clinical_events, 
    medications, 
    ons_deaths,
)


def last_matching_event_clinical_ctv3_before(codelist, start_date, where=True):
    return(
        clinical_events.where(where)
        .where(clinical_events.ctv3_code.is_in(codelist))
        .where(clinical_events.date.is_before(start_date))
        .sort_by(clinical_events.date)
        .last_for_patient()
    )

def last_matching_event_clinical_snomed_before(codelist, start_date, where=True):
    return(
        clinical_events.where(where)
        .where(clinical_events.snomedct_code.is_in(codelist))
        .where(clinical_events.date.is_before(start_date))
        .sort_by(clinical_events.date)
        .last_for_patient()
    )

def last_matching_med_dmd_before(codelist, start_date, where=True):
    return(
        medications.where(where)
        .where(medications.dmd_code.is_in(codelist))
        .where(medications.date.is_before(start_date))
        .sort_by(medications.date)
        .last_for_patient()
    )

def last_matching_event_apc_before(codelist, start_date, where=True):
    return(
        apcs.where(where)
        .where(apcs.primary_diagnosis.is_in(codelist) | apcs.secondary_diagnosis.is_in(codelist))
        .where(apcs.admission_date.is_before(start_date))
        .sort_by(apcs.admission_date)
        .last_for_patient()
    )

def last_matching_event_opa_before(codelist, start_date, where=True):
    return(
        opa_diag.where(where)
        .where(opa_diag.primary_diagnosis_code.is_in(codelist) | opa_diag.secondary_diagnosis_code_1.is_in(codelist))
        .where(opa_diag.appointment_date.is_before(start_date))
        .sort_by(opa_diag.appointment_date)
        .last_for_patient()
    )

def last_matching_event_clinical_snomed_between(codelist, start_date, end_date, where=True):
    return(
        clinical_events.where(where)
        .where(clinical_events.snomedct_code.is_in(codelist))
        .where(clinical_events.date.is_on_or_between(start_date, end_date))
        .sort_by(clinical_events.date)
        .last_for_patient()
    )

def last_matching_med_dmd_between(codelist, start_date, end_date, where=True):
    return(
        medications.where(where)
        .where(medications.dmd_code.is_in(codelist))
        .where(medications.date.is_on_or_between(start_date, end_date))
        .sort_by(medications.date)
        .last_for_patient()
    )

def matching_death_before(codelist, start_date, where=True):
    return(
        ((ons_deaths.underlying_cause_of_death.is_in(codelist)) | 
         (ons_deaths.cause_of_death_01.is_in(codelist)) | 
         (ons_deaths.cause_of_death_02.is_in(codelist)) | 
         (ons_deaths.cause_of_death_03.is_in(codelist)) | 
         (ons_deaths.cause_of_death_04.is_in(codelist)) | 
         (ons_deaths.cause_of_death_05.is_in(codelist)) | 
         (ons_deaths.cause_of_death_06.is_in(codelist)) | 
         (ons_deaths.cause_of_death_07.is_in(codelist)) | 
         (ons_deaths.cause_of_death_08.is_in(codelist)) | 
         (ons_deaths.cause_of_death_09.is_in(codelist)) | 
         (ons_deaths.cause_of_death_10.is_in(codelist)) | 
         (ons_deaths.cause_of_death_11.is_in(codelist)) | 
         (ons_deaths.cause_of_death_12.is_in(codelist)) | 
         (ons_deaths.cause_of_death_13.is_in(codelist)) | 
         (ons_deaths.cause_of_death_14.is_in(codelist)) | 
         (ons_deaths.cause_of_death_15.is_in(codelist))) & 
        (ons_deaths.date.is_before(start_date))
    )

def first_matching_event_clinical_ctv3_between(codelist, start_date, end_date, where=True):
    return(
        clinical_events.where(where)
        .where(clinical_events.ctv3_code.is_in(codelist))
        .where(clinical_events.date.is_on_or_between(start_date, end_date))
        .sort_by(clinical_events.date)
        .first_for_patient()
    )

def first_matching_event_clinical_snomed_between(codelist, start_date, end_date, where=True):
    return(
        clinical_events.where(where)
        .where(clinical_events.snomedct_code.is_in(codelist))
        .where(clinical_events.date.is_on_or_between(start_date, end_date))
        .sort_by(clinical_events.date)
        .first_for_patient()
    )

def first_matching_med_dmd_between(codelist, start_date, end_date, where=True):
    return(
        medications.where(where)
        .where(medications.dmd_code.is_in(codelist))
        .where(medications.date.is_on_or_between(start_date, end_date))
        .sort_by(medications.date)
        .first_for_patient()
    )

def first_matching_event_apc_between(codelist, start_date, end_date, where=True):
    return(
        apcs.where(where)
        .where(apcs.primary_diagnosis.is_in(codelist) | apcs.secondary_diagnosis.is_in(codelist))
        .where(apcs.admission_date.is_on_or_between(start_date, end_date))
        .sort_by(apcs.admission_date)
        .first_for_patient()
    )

def first_matching_event_opa_between(codelist, start_date, end_date, where=True):
    return(
        opa_diag.where(where)
        .where(opa_diag.primary_diagnosis_code.is_in(codelist) | opa_diag.secondary_diagnosis_code_1.is_in(codelist))
        .where(opa_diag.appointment_date.is_on_or_between(start_date, end_date))
        .sort_by(opa_diag.appointment_date)
        .first_for_patient()
    )

def matching_death_between(codelist, start_date, end_date, where=True):
    return(
        ((ons_deaths.underlying_cause_of_death.is_in(codelist)) | 
         (ons_deaths.cause_of_death_01.is_in(codelist)) | 
         (ons_deaths.cause_of_death_02.is_in(codelist)) | 
         (ons_deaths.cause_of_death_03.is_in(codelist)) | 
         (ons_deaths.cause_of_death_04.is_in(codelist)) | 
         (ons_deaths.cause_of_death_05.is_in(codelist)) | 
         (ons_deaths.cause_of_death_06.is_in(codelist)) | 
         (ons_deaths.cause_of_death_07.is_in(codelist)) | 
         (ons_deaths.cause_of_death_08.is_in(codelist)) | 
         (ons_deaths.cause_of_death_09.is_in(codelist)) | 
         (ons_deaths.cause_of_death_10.is_in(codelist)) | 
         (ons_deaths.cause_of_death_11.is_in(codelist)) | 
         (ons_deaths.cause_of_death_12.is_in(codelist)) | 
         (ons_deaths.cause_of_death_13.is_in(codelist)) | 
         (ons_deaths.cause_of_death_14.is_in(codelist)) | 
         (ons_deaths.cause_of_death_15.is_in(codelist))) & 
        (ons_deaths.date.is_on_or_between(start_date, end_date))
    )