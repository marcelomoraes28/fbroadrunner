from cerberus import Validator

PUBLICATION_SCHEMA = {
    'app_id': {'type': 'integer'},
    'link': {'type': 'string', 'default_setter': 'link', 'nullable': True},
    'display': {'type': 'string', 'default_setter': 'display',
                'nullable': True},
    'redirect_uri': {'type': 'string', 'default_setter': 'uri',
                     'nullable': True},
    'from': {'type': 'string', 'default_setter': 'from', 'nullable': True},
    'to': {'type': 'string', 'default_setter': 'to', 'nullable': True},
    'source': {'type': 'string', 'default_setter': 'source', 'nullable': True},
}

MESSAGE_SCHEMA = {
    'app_id': {'type': 'integer'},
    'redirect_uri': {'type': 'string', 'default_setter': 'uri',
                     'nullable': True},
    'link': {'type': 'string', 'default_setter': 'link', 'nullable': True},
    'display': {'type': 'string', 'default_setter': 'display',
                'nullable': True},
    'to': {'type': 'string', 'default_setter': 'to', 'nullable': True}
}


class CustomNormalizer(Validator):
    def _normalize_default_setter_link(self, document):
        return self.document['default_link']

    def _normalize_default_setter_display(self, document):
        return self.document['default_display']

    def _normalize_default_setter_uri(self, document):
        return self.document['default_redirect_uri']

    def _normalize_default_setter_from(self, document):
        return self.document['default_from']

    def _normalize_default_setter_to(self, document):
        return self.document['default_to']

    def _normalize_default_setter_source(self, document):
        return self.document['default_source']
