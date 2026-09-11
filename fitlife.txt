package aula2;


/**
 * Encapsulamento
 *  - private
 *  - protected*
 *  -public
 */

public class Televisao {

    private int canal = 1;
    private int volume = 10;
    private boolean ligado = false;
    private String marca = "Samsung";

    //Métodos de acesso e modificadores, respectivamente- getters() e setters()

    public int getCanal() {
        return canal;
    }

    public void setCanal(int canal) {
        this.canal = canal;
    }

    public int getVolume() {
        return volume;
    }

    public void setVolume(int volume) {
        this.volume = volume;
    }

    public boolean getLigado() {
        return ligado;
    }

    public void setLigado(boolean ligado) {
        this.ligado = ligado;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
        }
}
