// cwe-snippets, snippets_2/non-compliant/Java/0106.java

<bean id="testService" class="example.TestServiceImpl"/>
<bean class="org.springframework.jms.remoting.JmsInvokerServiceExporter">
        <property name="serviceInterface" value="example.TestService"/>
        <property name="service" ref="testService"/>
</bean>