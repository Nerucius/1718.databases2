<%@ page session="true" contentType="text/html; charset=ISO-8859-1" %>
<%@ taglib uri="http://www.tonbeller.com/jpivot" prefix="jp" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jstl/core" %>


<jp:mondrianQuery id="query01" jdbcDriver="org.gjt.mm.mysql.Driver" jdbcUrl="jdbc:mysql://carrotpiracy.com:3306/menjaub" catalogUri="/WEB-INF/queries/menjaub.xml" jdbcUser="menjaub" jdbcPassword="menjaub" connectionPooling="false">

SELECT {
	[Measures].[amount], [Measures].[orders],[Measures].[item sales],[Measures].[customers]
} ON COLUMNS,
{
	[Date]
} ON ROWS

FROM [Order Items]

</jp:mondrianQuery>

<!--
SELECT {
	[Measures].[people], [Measures].[fee],[Measures].[no show ratio]
} ON COLUMNS,
{
	[Booking Date]
} ON ROWS

FROM [Bookings]
-->

<!-- 
SELECT {
	[Measures].[orders], [Measures].[amount], [Measures].[item sales], [Measures].[customers]
} ON COLUMNS,
{
	[Date]
} ON ROWS

FROM [Order Items]
-->



<c:set var="title01" scope="session">MenjaUB MDX Query</c:set>
