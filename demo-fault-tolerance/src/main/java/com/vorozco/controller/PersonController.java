package com.vorozco.controller;

import com.vorozco.model.Person;

import org.eclipse.microprofile.faulttolerance.Fallback;
import org.eclipse.microprofile.faulttolerance.Retry;
//import org.eclipse.microprofile.faulttolerance.Timeout;

import javax.ws.rs.Path;
import javax.ws.rs.GET;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.logging.Logger;

@Path("/persons")
@Produces(MediaType.APPLICATION_JSON)
public class PersonController {
    List<Person> personList = new ArrayList<>();
    Logger LOGGER = Logger.getLogger("Demologger");

    @GET
    //@Timeout(value=5000L)   //Si tarda mas de 5 segundos en responder
    @Retry(maxRetries = 4)    //Si falla
    @Fallback(fallbackMethod = "getPersonFallbackList")    //Metodo alternativo
    public List<Person> getPersonList(){
        LOGGER.info("Ejecutando person List");
        doFail();
        //doWait();
        return this.personList;
    }
    
    public List<Person> getPersonFallbackList(){
        var person = new Person(-1, "Victor", "me@vorozco.com");
        return List.of(person);
    }

    public void doWait(){
        var random = new Random();  //Se genera de manera aleatoria
        try {
            LOGGER.warning("Haciendo un sleep");
            Thread.sleep((random.nextInt(10)+4)*1000L);
        } catch (Exception e) {
            //TODO: handle exception
        }
    }

    public void doFail(){
        var random = new Random();  //Se genera de manera aleatoria
        if(random.nextBoolean()){
            LOGGER.warning("Se produjo una falla");
            throw new RuntimeException("La implementación fallo");
        }
    }
}
