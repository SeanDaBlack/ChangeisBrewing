XPATHS_1 = {

    'username' : '//*[@id="dialogTemplate-dialogForm-userName"]',
    'pass': '//*[@id="dialogTemplate-dialogForm-password"]',
    'pass-retype': '//*[@id="dialogTemplate-dialogForm-passwordConfirm"]',
    'email': '//*[@id="dialogTemplate-dialogForm-email"]',
    'email-retype': '//*[@id="dialogTemplate-dialogForm-emailConfirm"]',

}

XPATHS_2 = {

    'first_name': '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-cpi-cfrmsub-frm-dv_cs_candidate_personal_info_FirstName"]',
    'perfered_first_name' : '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-cpi-cfrmsub-frm-dv_cs_candidate_personal_info_UDFCandidatePersonalInfo_Preferred_32_Name"]',
    'last_name': '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-cpi-cfrmsub-frm-dv_cs_candidate_personal_info_LastName"]',
    'zip': '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-cpi-cfrmsub-frm-dv_cs_candidate_personal_info_ZipCode"]',
    'pn': '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-cpi-cfrmsub-frm-dv_cs_candidate_personal_info_HomePhone"]',

    'work_experience_employer' : '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_3-we-wei-0-frm-dv_cs_experience_Employer"]',
    'work_experinece_title' : '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_3-we-wei-0-frm-dv_cs_experience_JobFunction"]',


}

XPATHS_3 = {


    'region' : '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-cpi-cfrmsub-frm-dv_cs_candidate_personal_info_ResidenceLocation-0"]',
    'state' : '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-cpi-cfrmsub-frm-dv_cs_candidate_personal_info_ResidenceLocation-1"]',
    'city' : '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-cpi-cfrmsub-frm-dv_cs_candidate_personal_info_ResidenceLocation-2"]',


    'sb_experience' : '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-cpi-cfrmsub-frm-dv_cs_candidate_personal_info_UDFCandidatePersonalInfo_Prev_Employ"]',


}
XPATH_AVAL = {

    'hours_week1': '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_1-careerSectionMultipleCustomForm-cfrm-cfrmsub-frm-dv_cs_workcondition_HoursPerWeekWilling"]',
    'hours_week2': '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_1-careerSectionMultipleCustomForm-cfrm-cfrmsub-frm-dv_cs_workcondition_HoursPerWeekPreferred"]',
    'hours_holi' : '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_1-careerSectionMultipleCustomForm-cfrm-cfrmsub-frm:dv_cs_workcondition_IsAvailableHolidays"]',
    'hours_times' : '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_2-shiftAvailabilityBlock-AllShift"]/span/span/span/span',


    'current_job' : '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_3-we-wei-0-frm:dv_cs_experience_CurrentEmployer"]',

    
}

# PAGE 2
UPLOAD_A_RESUME_BUTTON = '//*[@id="editTemplateMultipart-editForm-content-ftf-gp-j_id_id16pc8-page_0-AttachedFilesBlock-uploadedFile"]'
ATTACH_RESUME = '//*[@id="editTemplateMultipart-editForm-content-ftf-gp-j_id_id16pc8-page_0-AttachedFilesBlock-attachFileCommand"]'

# PAGE 3
XPATH_QUALS = {
    'Quals_1' : '/html/body/div[3]/form/span/span[2]/span[4]/table/tbody/tr/td/span[4]/span[3]/fieldset[1]/span[1]/label/input',
    'Quals_2' : '/html/body/div[3]/form/span/span[2]/span[4]/table/tbody/tr/td/span[4]/span[3]/fieldset[2]/span[1]/label/input',
    'Quals_3' : '/html/body/div[3]/form/span/span[2]/span[4]/table/tbody/tr/td/span[4]/span[3]/fieldset[3]/span[1]/label/input',
    'Quals_4' : '/html/body/div[3]/form/span/span[2]/span[4]/table/tbody/tr/td/span[4]/span[3]/fieldset[4]/span[1]/label/input',

}

# PAGE 4
XPATH_EEO = {

    'EEO_1' : '/html/body/div[3]/form/span/span[2]/span[4]/table/tbody/tr/td/span[4]/fieldset[1]/span[2]/label/input',
    'EEO_2' : '/html/body/div[3]/form/span/span[2]/span[4]/table/tbody/tr/td/span[4]/fieldset[2]/span[3]/label/input',
    'EEO_3' : '/html/body/div[3]/form/span/span[2]/span[4]/table/tbody/tr/td/span[4]/fieldset[3]/span[3]/label/input',

}

XPATH_RACES = [

    '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-3-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__26260130812"]',
    '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-3-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__26360130812"]',
    '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-3-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__26460130812"]',
    '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-3-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__26560130812"]',
    '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-3-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__26660130812"]',
    '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-3-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__26760130812"]',              
    '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-3-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__26860130812"]',
]




XPATH_VOL = {
    "VOL_NAME" : '/html/body/div[3]/form/span/span[2]/span[4]/table/tbody/tr/td/span[4]/div[2]/div/div[2]/div/div/input[1]',
    "VOL_DATE" : '/html/body/div[3]/form/span/span[2]/span[4]/table/tbody/tr/td/span[4]/div[2]/div/div[2]/div/div/input[2]',
    "VOL_no" : '/html/body/div[3]/form/span/span[2]/span[4]/table/tbody/tr/td/span[4]/div[2]/div/div[2]/div/div/input[4]'
}

XPATH_QUEST = {

    'QUEST_2' : '//*[@id="SurveyControl_Question11396"]/div/label[2]',
    'QUEST_3' : '//*[@id="SurveyControl_Question11397"]/div/label[2]',
    'QUEST_4' : '//*[@id="SurveyControl_Question914"]/div/label[2]',
    'QUEST_5' : '//*[@id="SurveyControl_Question11361"]/div/label[2]',
    'QUEST_6' : '//*[@id="SurveyControl_Question1244"]/div/label[2]',
    'QUEST_7' : '//*[@id="SurveyControl_Question11392"]/div/label[2]',
    'QUEST_8' : '//*[@id="SurveyControl_Question942"]/div/label[2]',
    'QUEST_RETURN' : '/html/body/form/div[4]/span/div[1]/div/div[8]/div/input',

}

RESUME_UPLOAD_PARTNER = '//*[@id="editTemplateMultipart-editForm-content-ftf-gp-j_id_id16pc8-page_0-ResumeParsingBlock-UploadResumeBlock-resumeUploadRadio_2"]'
ATTACH_RESUME_PARTNER = '//*[@id="editTemplateMultipart-editForm-content-ftf-gp-j_id_id16pc8-page_0-ResumeParsingBlock-UploadResumeBlock-ResumeUploadInputFile"]'


APPLY_NOW_BUTTON_1 = '//*[@id="requisitionDescriptionInterface.UP_APPLY_ON_REQ.row1"]'
PRIVACY_ACCEPT = '//*[@id="dialogTemplate-dialogForm-StatementBeforeAuthentificationContent-ContinueButton"]'
NEW_CANIDATE_BUTTON = '//*[@id="dialogTemplate-dialogForm-login-register"]'
REGISTER_ACCOUNT = '//*[@id="dialogTemplate-dialogForm-defaultCmd"]'

CONTINUE = '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]'
CONTINUE2 = '//*[@id="editTemplateMultipart-editForm-content-ftf-saveContinueCmdBottom"]'
FULL_NAME = '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-eSignatureBlock-cfrmsub-frm-dv_cs_esignature_FullName"]'

SUBMIT_APP = '//*[@id="et-ef-content-ftf-submitCmdBottom"]'

QUEST = '/html/body/div[3]/form/span/span[2]/span[4]/table/tbody/tr/td/span[5]/span/span/a/span[1]'
QUEST_SUBMIT = '/html/body/form/div[4]/span/div[1]/div/div[2]/div/input'

SUPER_QUAL = '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-preq-j_id_id7pc10-page__1-q-j_id_id2pc11-4-qr_com.taleo.functionalcomponent.prescreening.entity.question.PossibleAnswer__146937"]'