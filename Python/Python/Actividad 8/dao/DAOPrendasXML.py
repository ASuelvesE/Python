
from common.utils import write

class DAOPrendasXML:

    def writeHTML(self,prendas):
        htmlContent = '<html><body>'
        for prenda in prendas:
            htmlContent += '<div>'
            htmlContent += '<p>'+prenda.tipo+'</p>'
            htmlContent += '<p>'+prenda.marca+'</p>'
            htmlContent += '<p>'+prenda.color+'</p>'
            htmlContent += '<p>'+prenda.talla+'</p>'
            htmlContent += '</div>'
        htmlContent += '</body></html>'
        write('./data/output.html', htmlContent)


    def writeXML(self,prendas,ruta):
        htmlContent = '<armario>'
        for prenda in prendas:
            htmlContent += '<prenda '
            htmlContent += 'tipo="'+prenda.tipo+'" '
            htmlContent += 'marca="'+prenda.marca+'" '
            htmlContent += 'color="'+prenda.color+'" '
            htmlContent += 'talla="'+prenda.talla+'" '
            htmlContent += ' />'
        htmlContent += '</armario>'
        write(ruta, htmlContent)

    def resultadosXML(self,prendas):
        contenido = "<armario>"
        contenido += prendas
        contenido += "</armario>"
        write('./data/resultados.xml', contenido)
