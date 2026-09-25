class GeminiDocumentGenerator:

    def generate_document(self, data):
        document_type = data.get("document_type", "Document")

        return f"{document_type} generated successfully."