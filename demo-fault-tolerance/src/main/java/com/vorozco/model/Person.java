package com.vorozco.model;

public class Person {
    private Integer personId;
    private String name;
    private String email;

    public Person(){

    }

    public Person(Integer personId, String name, String email){
        this.personId = personId;
        this.name = name;
        this.email = email;
    }

    public Integer getPersonId(){
        return personId;
    }
    public void setPersonId(Integer personId){
        this.personId = personId;
    }
    public String getName(){
        return name;
    }
    public void setName(String name){
        this.name = name;
    }
    public String getEmail(){
        return email;
    }
    public void setEmail(String email){
        this.email = email;
    }
}
