------------------------------------------------
-- Design: tb_voter_trm
-- Entity: tb_voter_trm
-- Author: Lucas Cunha e Luiz Zimmermann
-- Rev.  : 1.0
-- Date  : 07/11/2020
------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;
 
entity tb_voter_trm  is
-- empty
end tb_voter_trm; 

architecture arch_1 of tb_voter_trm  is

-- DUT component
component voter_trm is
port (i_CLK 	: in std_logic;
	   i_A  		: in  std_logic_vector (15 downto 0);  -- data input
      i_B   	: in  std_logic_vector (15 downto 0);  -- data input
      i_C   	: in  std_logic_vector (15 downto 0);  -- data input
	   i_clr_n 	: in std_logic;
      o_S   	: out std_logic_vector (15 downto 0)); -- data output
end component;

signal  w_A, w_B, w_C, w_S : std_logic_vector(15 downto 0);
signal  w_CLK, w_CLR : std_logic;
constant c_CLK_PERIOD : time := 2 ns;
begin

  -- Connect DUT
  u_DUT: voter_trm  port map( i_CLK => w_CLK,
										i_A => w_A,
										i_B => w_B,
										i_C => w_C,
										i_clr_n => w_CLR,
										o_S => w_S);
                            
  p_CLK: process
  begin
  	w_CLK <= '0';
    wait for c_CLK_PERIOD/2;  
    w_CLK <= '1';
    wait for c_CLK_PERIOD/2;  
  end process p_CLK;                          
                           
  process
  begin
   
   	w_CLR <= '1';
		w_A <= "0000000000000000";
		w_B	<= "0000000000000000";
		w_C <= "0000000000000000";
    wait  for 2*c_CLK_PERIOD;
    assert(w_S="0000000000000000") report "Fail @ 00 at S1" severity error;

   	w_A <= "1111111111111111";
    w_B	<= "0000000000000000";
    w_C <= "0000000000000000";
    wait  for 2*c_CLK_PERIOD;
    assert(w_S="0000000000000000") report "Fail @ 01 at S1" severity error;

   	w_A <= "1111111111111111";
    w_B	<= "1111111111111111";
    w_C <= "0000000000000000";
    wait  for 2*c_CLK_PERIOD;
    assert(w_S="1111111111111111") report "Fail @ 01 at S1" severity error;

   	w_A <= "1111110000111111";
    w_B	<= "0000000000000000";
    w_C <= "1111110000111111";
    wait  for 2*c_CLK_PERIOD;
    assert(w_S="1111111111111111") report "Fail @ 01 at S1" severity error;
    
    w_A <= "0000000000000000";
    w_B	<= "1111111111110011";
    w_C <= "1111111111111111";
    wait  for 2*c_CLK_PERIOD;
    assert(w_S="1111111111111111") report "Fail @ 01 at S1" severity error;

    -- Clear inputs
    w_A 	<= "0000000000000000";
    w_B		<= "0000000000000000";
 
    assert false report "Test done." severity note;
    wait;
  end process;
end arch_1;