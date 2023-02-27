import json
from collections import namedtuple

from src.main import Osc


def main():
    client_id = ""
    client_secret = ""
    osc = Osc.create_instance(client_id, client_secret)

    try:
        osc.set_response_listening(process_pipeline_result)
        pipeline_response = signup()
        process_pipeline_result(pipeline_response)
    except Exception as e:
        print(e)


def process_pipeline_result(pipeline_response):
    if not pipeline_response:
        print("Pipeline: error")
        return

    status = pipeline_response.get_status()
    if status == "SIGNUP_ANALISIS":
        print("Pipeline: {} (cadastro em analise)".format(pipeline_response.get_id()))
    elif status == "SIGNUP_COMPLETED":
        print("Pipeline: {} (enviar solicitação de proposta)".format(pipeline_response.get_id()))
        proposal(pipeline_response.get_id())
    elif status == "SIGNUP_DENIED":
        print("Pipeline: {} (cadastro reprovado)".format(pipeline_response.get_id()))
    elif status == "PROPOSAL_ANALISIS":
        print("Pipeline: {} (proposta em analise)".format(pipeline_response.get_id()))
    elif status == "PROPOSAL_CREATED":
        print("Pipeline: {} (proposta(s) criadas)".format(pipeline_response.get_id()))
        proposals = pipeline_response.get_proposals()
        pendent_doc = True

    proposals = []

    for credit in proposals:
        if credit.getHasDocuments():
            document_request = None
            for pendent_document in credit.getPendentDocuments():
                if pendent_document == "SELF":
                    document_request = DocumentRequest(DocumentType.SELF, MimeType.CODE_01, "name", "base 64")
                elif pendent_document == "ADDRESS_PROOF":
                    document_request = DocumentRequest(DocumentType.ADDRESS_PROOF, MimeType.CODE_01, "name",
                                                       "base 64")
                elif pendent_document == "IDENTITY_BACK":
                    document_request = DocumentRequest(DocumentType.IDENTITY_BACK, MimeType.CODE_01, "name",
                                                       "base 64")
                elif pendent_document == "IDENTITY_FRONT":
                    document_request = DocumentRequest(DocumentType.IDENTITY_FRONT, MimeType.CODE_01, "name",
                                                       "base 64")
                elif pendent_document == "INCOME_PROOF":
                    document_request = DocumentRequest(DocumentType.INCOME_PROOF, MimeType.CODE_01, "name",
                                                       "base 64")
                br.com.fitbank.requests.Document.putDocument(osc, document_request, pipeline_response.getId())

        if credit.getHasContracts():
            getContracts(credit.customerServiceNumber)

                s = signContracts(credit.customServiceNumber, credit.signContractRequest)
                signContracts = [s.getAceptedCheckSum()]

            signedSignContractRequest = SignContractRequest(signContracts, None)
            signContracts(osc, customServiceNumber, signedSignContractRequest)

    if pipelineResponse.getStatus() == "PROPOSAL_APPROVED":
        print("Pipeline: {} (proposta aprovada)".format(pipelineResponse.getId()))
    elif pipelineResponse.getStatus() == "PROPOSAL_DENIED":
        print("Pipeline: {} (proposta reprovada)".format(pipelineResponse.getId()))
    else:
        print("Pipeline: {}".format(pipelineResponse.getId()))


def signup():
    data = ""
    signupRequest = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    return Osc.get_instance().signup(signupRequest)


def proposal(id):
    data = ""
    proposalRequest = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    return Osc.get_instance().proposal(proposalRequest, id)

def getContracts(customerServiceNumber):
    return Osc.get_instance().getContracts(customerServiceNumber)

def signContracts(customerServiceNumber, signContractRequest):
    return Osc.get_instance().signContracts(customerServiceNumber, signContractRequest)
