from django.contrib import admin
from . import models

all_models = [
    models.PSCEDClassification,
    models.Classification,
    models.Collaboration,
    models.Publication,
    models.AuthorRole,
    models.Author,
    models.ConferenceLevel,
    models.Conference,
    models.BudgetType,
    models.Budget,
    models.CollaborationType,
    models.Record,
    models.RecordType,
    models.CheckedRecord,
    models.ResearchRecord,
    models.PublicationLevel,
    models.Upload,
    models.RecordUpload,
    models.CheckedUploadsStatusType,
    models.CheckedUpload,
]
admin.site.register(all_models)
