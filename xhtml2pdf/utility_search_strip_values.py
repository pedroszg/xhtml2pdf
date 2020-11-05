from reportlab.platypus import Paragraph
import re


class utility_search_strip:

    def search_strip_str(self, flowable):
        text = flowable.text
        result = re.search(r'[\w.-]+#[\w.-]+', text)
        text = text.lstrip(result.group())
        text = text.lstrip()
        return text

    def searching_index(self, flowable):
        index = re.search(r'-\w+', flowable.text)
        index = index.group()
        index = index.lstrip('-')
        return index

    def clean_text_flowables(self):
        cleans_flowables = []
        for flow in self.flowElements:
            if isinstance(flow, Paragraph):
                text = self.search_strip_str(flow)
                nf = Paragraph(text, self.style)
                cleans_flowables.append(nf)
            else:
                cleans_flowables.append(flow)
        self.flowElements = cleans_flowables

    def clean_text_flowable(self, flow):
        text = self.search_strip_str(flow)
        nf = Paragraph(text, self.style)
        return nf