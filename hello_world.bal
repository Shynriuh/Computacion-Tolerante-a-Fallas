import ballerina/http;
import ballerina/log;
import ballerinax/kubernetes;

@kubernetes:Service {
    serviceType:"NodePort",
    name:"helloworldservice"
}

endpoint http:Listener listener {
    port:9095
};

@kubernetes:Deployment {
    image: "helloworldservice",
    name: "helloworldservice",
    dockerHost:"tcp://<minikube ip>:2376", // IP can be obtained via `sudo minikube ip` command
    dockerCertPath:"<Home Dir>/.minikube/certs",
    singleYAML:true
}@http:ServiceConfig {basePath:"/helloworld"}
service<http:Service> hello bind listener {
    @http:ResourceConfig{
        path: "/",
        methods: ["GET"]
    }
    sayHello(endpoint caller, http:Request req) {
        http:Response res = new;

        res.setPayload("Hello, World!\n");

        caller->respond(res) but { error e => log:printError(
           "Error sending response", err = e) };
    }
}
