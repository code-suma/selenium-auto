package com.inetbanking.testCases;

import java.io.IOException;

import org.testng.Assert;
import org.testng.annotations.Test;

import com.inetbanking.pageObjects.LoginPage;

public class TC_LoginTest_001 extends BaseClass {
	@Test
	public void LoginTest() {
		System.out.println("Base URL is " + baseURL);
		driver.get(baseURL);
		logger.info("URL is opened");
		
		LoginPage lp = new LoginPage(driver);
		try {
			Thread.sleep(2000) ;
		} catch (InterruptedException e) {	
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		lp.setUserName(username);
		logger.info("Entered username");
		lp.setPassword(password);
		logger.info("Enter password");
		try {
			Thread.sleep(4000);
			logger.info("Submitting user credentials");
			lp.clickSubmit();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		System.out.println("Title is " + driver.getTitle());
		if (driver.getTitle().contains("Guru99 Bank Manager HomePage")) 
		{
			Assert.assertTrue(true);
			logger.info("Login test passed");
		} 
		else
		{	try {
			captureScreen(driver,"LoginTest");
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
			Assert.assertTrue(false);
			logger.info("Login test failed");

		}

	}
	

	

}

