<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">

        <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
                <title>Laptops</title>
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
                      crossorigin="anonymous"/>
            </head>
            <body>
                <div class="container mt-3">
                    <table class="table table-bordered">
                        <tbody>
                            <tr>
                                <th>Зображення</th>
                                <th>Назва</th>
                                <th>Ціна</th>
                                <th>Опис</th>
                            </tr>
                            <xsl:for-each select="//laptop">
                                <tr>
                                    <td>
                                        <img src="{image}" width="250px"/>
                                    </td>
                                    <td>
                                        <strong>
                                            <xsl:value-of select="@name"/>
                                        </strong>
                                    </td>
                                    <td>
                                        <xsl:value-of select="price"/>
                                        грн
                                    </td>
                                    <td>
                                        <xsl:value-of select="description"/>
                                    </td>
                                </tr>
                            </xsl:for-each>
                        </tbody>
                    </table>
                </div>
            </body>
        </html>

    </xsl:template>
</xsl:stylesheet>