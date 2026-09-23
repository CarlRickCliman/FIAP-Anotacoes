package aula1;

public class Carro {

    private String marca;
    private String modelo;
    private String cor;
    private String ano;
    private float preco;

    public Carro(){

        this.marca = "Chevrolet";
        this.modelo = "Saveiro";
        this.cor = "Preto";
        this.ano = "2026";
        this.preco = 119000;


    }

    public Carro(String marca, String modelo, float preco) {
        this.marca = marca;
        this.modelo = modelo;
        this.preco = preco;

    }

    public Carro(String marca, String modelo, String cor, String ano, float preco) {
        this.marca = marca;
        this.modelo = modelo;
        this.cor = cor;
        this.ano = ano;
        this.preco = preco;
    }

    public void exibirInfo() {

        System.out.println("Marca: " + marca);
        System.out.println("Modelo: " + modelo);
        System.out.println("Cor: " + cor);
        System.out.println("Ano: " + ano);
        System.out.println("Preço: " + preco);

    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public String getCor() {
        return cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }

    public String getAno() {
        return ano;
    }

    public void setAno(String ano) {
        this.ano = ano;
    }

    public float getPreco() {
        return preco;
    }

    public void setPreco(float preco) {
        this.preco = preco;
    }
}
