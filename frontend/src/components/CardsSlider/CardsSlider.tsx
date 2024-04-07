import { ReactElement } from 'react';
import './CardsSlider.scss';
import CardListHeader from '../CardListHeader/CardListHeader.tsx';
import { IServiceExtended } from '../../utils/interfaces/interfaces.ts';
import { Swiper, SwiperSlide } from 'swiper/react';
import 'swiper/scss';
import 'swiper/scss/pagination';
import ServiceCard from '../ServiceCard/ServiceCard.tsx';

interface ICardsSliderProps {
  title: string;
  cardType: 'square' | 'big';
  link: string;
  items: IServiceExtended[];
  slidesPerView: number;
}

function CardsSlider(props: ICardsSliderProps): ReactElement {
  return (
    <section className="cards-slider">
      <CardListHeader title={props.title} link={props.link} />
      <div className="cards-slider__wrapper">
        <Swiper tag="ul" slidesPerView={props.slidesPerView} spaceBetween={8}>
          {props.items.map((card, index) => (
            <SwiperSlide tag="li" key={`card-${index}`}>
              <ServiceCard card={card} cardType={props.cardType} />
            </SwiperSlide>
          ))}
        </Swiper>
      </div>
    </section>
  );
}

export default CardsSlider;
