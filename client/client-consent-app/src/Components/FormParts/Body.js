import React from "react";
import "./style/Form.css";
import Typography from "@material-ui/core/Typography";

const Body = () => {
  return (
    <div className="Body">
      <div>
        <Typography variant="h6" component="div">
          Titel van onderzoek: <br />
          <span className="Titles"> Hoe denk jij over deze beroepen?</span>
        </Typography>
        <Typography variant="h6" component="div">
          Hoofdonderzoeker(s):
          <br />
          <span className="Titles">
            Felienne Hermans,
            <br /> Fenia Aivaloglou
          </span>
        </Typography>
        <Typography variant="h6" component="div">
          Uitvoerend onderzoeker(s): :
          <br />
          <span className="Titles">Felienne Hermans,
            <br /> Fenia Aivaloglou
            <br /> Shirley de Wit</span>
        </Typography>
        <Typography variant="h6" component="div">
          Onderzoeksgroep: <br />
          <span className="Titles">
            {" "}
            Programming Education Research Group, Universiteit Leiden
          </span>
        </Typography>
      </div>

      <Typography variant="h6" component="div" className="Information">
        Beste deelnemer,
      </Typography>
      <Typography variant="body2" component="div" className="Paragraph">
        Fijn dat je meedoet aan Science Live, het onderzoeksprogramma van NEMO
        Science Museum. Het onderzoek waar je aan meewerkt wordt uitgevoerd door
        onderzoekers van Universiteit Leiden. Voor deelname aan dit onderzoek moet
        een ouder/voogd toestemming geven.
      </Typography>
      <Typography variant="body2" component="div" className="Paragraph">
        In dit onderzoek leren we over hoe kinderen denken over een aantal beroepen 
        en we hebben daar jouw hulp voor nodig! Je gaat een spelletje doen, een 
        aantal vragen beantwoorden en een video bekijken. In dit onderzoek zijn er 
        geen foute antwoorden, je doet het dus altijd goed! Help jij ons mee met 
        ons onderzoek?  
      </Typography>
      <Typography variant="body2" component="div" className="Paragraph">
        Er wordt geen beloning gegeven voor deelname. Voor dit onderzoek geldt
        de reguliere aansprakelijkheidsverzekering van Universiteit Leiden.
      </Typography>
      <Typography variant="body2" component="div" className="Paragraph">
        Het onderzoek duurt ongeveer 15 minuten.
        <b>
          {" "}
          Je mag het onderzoek op elk gewenst moment stoppen, zonder opgave van
          reden.{" "}
        </b>
        Maak dit kenbaar aan de aanwezige wetenschapper.
      </Typography>
      <Typography variant="body2" component="div" className="Paragraph">
        Verder willen je vragen om na het onderzoek niet te vertellen aan andere
        NEMO-bezoekers wat je precies moest doen, ook niet aan je familie en
        vrienden waarmee je NEMO bezoekt. Zij willen misschien ook deelnemen aan
        dit onderzoek en deze informatie kan de resultaten beïnvloeden.
      </Typography>
      <Typography variant="h6" component="div" className="Information">
        Persoonsgegevens
      </Typography>
      <Typography variant="body2" component="div" className="Paragraph">
        Alle onderzoeksgegevens blijven vertrouwelijk en worden anoniem
        verwerkt. De onderzoeksgegevens worden losgekoppeld van namen; alleen de
        hoofdonderzoeker houdt toegang tot namen. 10 jaar na het onderzoek
        worden de namen definitief verwijderd. U kunt te allen tijde de
        faculteit LIACS, Universiteit Leiden vragen om verwijdering van uw
        gegevens.
      </Typography>
      <Typography variant="body2" component="div" className="Paragraph">
        De geanonimiseerde gegevens zullen worden gebruikt voor onderzoek. Ze
        worden niet gebruikt door NEMO Science Museum.
      </Typography>

      <Typography variant="body2" component="div" className="Paragraph">
        <b>
          {" "}
          Geachte ouder/voogd, we verzoeken je om dit toestemmingsformulier in
          te vullen en te ondertekenen. Let op, in dit formulier kunt u toestemming 
          geven voor meerdere kinderen. Klik hiervoor op de blauwe knop met het '+'-symbool. 
        </b>
      </Typography>
      <Typography variant="body2" component="div" className="Paragraph">
        Hierbij verklaart de ouder/voogd van onderstaande minderjarigen aan
        NEMO (Stichting Nationaal Centrum voor Wetenschap en Technologie),
        gevestigd aan Oosterdok 2 te Amsterdam dat onderstaande minderjarigen 
        heeft/hebben deelgenomen aan het op het bovengenoemde en beschreven onderzoek.
        Door ondertekening van dit formulier geef ik uitdrukkelijk toestemming 
        tot deelname aan het onderzoek binnen NEMO’s Science Live programma. 
      </Typography>
      <Typography variant="body1" component='div' className="Paragraph">
          <b>
          Op {new Date().getDate()} / {new Date().getMonth()+1} / {new Date().getFullYear()}
          </b>
      </Typography>
    </div>
  );
};

export default Body;
