/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package GitHub2023;


/**
 *
 * @author eugene
 */
public class DbRole {
    String sid, pw;
    boolean showRecordByDbRole=false;
    
    public DbRole(String parameters){
        String copyStr=parameters.toString();  // stack parameter is not a local string
        
        if(!parameters.isBlank() && !parameters.isEmpty()){
            copyStr=parameters.toString();
            
        String[] y=copyStr.split(CSV._columnSeparator);
       sid=y[0]; pw=y[1];}
    }
    
    
    
}
