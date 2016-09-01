<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="3.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions" xmlns:mm="http://www.csp.com/Securitization/marks-common-functions">
	<xsl:output method="text" version="1.0" encoding="UTF-8" indent="yes"/>
	
	<xsl:strip-space elements="*"/>
	
	<!-- Parameters -->

	
	<!-- Functions -->

	
	<!-- complext elements - elemenets with descendants that are also elements -->
	<!--
	<xsl:template match="xs:element[descendant::xs:element][@name]"> 
		<xsl:text>&#xa;</xsl:text>
		<xsl:value-of select="@name"/>
		<xsl:text>&#xa;</xsl:text>
		<xsl:apply-templates/>
	</xsl:template>
	-->
	
	<!-- simple elements -->
	<!-- REVIEW FOR REMOVAL
	<xsl:template match="*/xs:element[not(descendant::xs:element)][@name]"> 
		<xsl:value-of select="current()/@name"/>
		<xsl:text>&#xa;</xsl:text>
	</xsl:template>
	-->
	

	<!-- simple elements -->
	<xsl:template match="/" >
		<xsl:text>Element Hierarchy</xsl:text>
		<xsl:text>&#xa;</xsl:text>
		<xsl:text>&#xa;</xsl:text>	
		<xsl:apply-templates select="descendant::xs:element"/>

	</xsl:template>
	
	<xsl:template match="descendant::xs:element" >
		<xsl:param name="level" select="count(./ancestor::*)"/>
		<xsl:for-each select=".">
			<xsl:sequence select="fn:string-join(for $i in 1 to $level return '  ', ' ')"/>
			<xsl:choose>
				<xsl:when test=".[@name][*]">
					<xsl:value-of select="@name"/>
				</xsl:when>
				<xsl:when test="@name">
					<xsl:value-of select="@name"/>
				</xsl:when>
				<xsl:when test="@ref">
					<xsl:value-of select="@ref"/>
				</xsl:when>
			</xsl:choose>
			<xsl:text>&#xa;</xsl:text>		
		</xsl:for-each>	
	</xsl:template>
	



	<!-- reference elements -->	
	<!--	
	<xsl:template match="descendant::xs:element[@ref]">
		<xsl:for-each select=".">
			<xsl:value-of select="@ref"/>
			<xsl:text>&#xa;</xsl:text>		
		</xsl:for-each>
	</xsl:template>
	-->
	
	
	<!-- referenced elements -->
	<!--
	<xsl:template match="*/xs:element[not(descendant::xs:element)][@ref]"> 
		<xsl:value-of select="current()/@ref"/>
		<xsl:text>&#xa;</xsl:text>
		<xsl:call-template name="lookup-reference-element">
			<xsl:with-param name="element-name" select="current()[@ref]"/>
		</xsl:call-template>
	</xsl:template>
	-->
	
	
	<!--
	<xsl:template name="lookup-reference-element">
		<xsl:param name="element-name"/>
		<xsl:for-each select="/xs:schema/xs:element[@name = $element-name]">
			<xsl:apply-templates/>
		</xsl:for-each>
	</xsl:template>
	-->
	
	
	<!--
	<xsl:template name="buildElementTree">
		<xsl:param name="element-node"/>
		<xsl:param name="node-tree"/>
		<xsl:param name="tabCount" as="xs:integer"/>
		
		<xsl:value-of select="$tabCount" />
		
		<xsl:choose>
			<xsl:when test="current()[not(descendant::xs:element)]">
				<xsl:value-of select="$element-node/@name"/>
			</xsl:when>
			<xsl:otherwise>
				<xsl:value-of select="$element-node/@name"/><xsl:text> has child nodes.</xsl:text>
				<xsl:for-each select="current()[descendant::xs:element]">
					<xsl:call-template name="buildElementTree">
						<xsl:with-param name="element-node" select="."/>
						<xsl:with-param name="tabCount" select="$tabCount + 1"/>
					</xsl:call-template>
				</xsl:for-each>
			</xsl:otherwise>
		</xsl:choose>
		
	</xsl:template>
	-->
	
	
</xsl:stylesheet>
