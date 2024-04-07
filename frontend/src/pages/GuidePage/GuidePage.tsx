import styled from 'styled-components';
import { Swiper, SwiperClass, SwiperSlide } from 'swiper/react';
import { Pagination } from 'swiper/modules';
import 'swiper/scss';
import 'swiper/scss/pagination';
import { useState } from 'react';
import { Button } from '@mui/material';
import { Link } from 'react-router-dom';
import guidePic1 from '../../images/other_images/guide1.png';
import guidePic2 from '../../images/other_images/guide2.png';

const Section = styled.section`
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-bottom: 28px;
  height: calc(100svh - 72px);
`;

const MainWrapper = styled.div`
  flex: 1 0 auto;
  width: 100%;
  max-width: 100%;
  max-height: 100vh;
  min-height: 0;
  min-width: 0;
`;

const GuideSwiperSlide = styled(SwiperSlide)`
  & img {
    width: 100%;
  }
`;

const Title = styled.h1`
  text-align: left;
`;

const SubTitle = styled.p`
  text-align: left;
  color: var(--grey-1);
`;

const LinkWrapper = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  align-self: flex-end;
`;

const OnbordingLink = styled(Link)<{ $visibility: boolean }>`
  display: block;
  margin-top: 20px;
  width: max-content;
  text-decoration: none;
  color: var(--navy-blue-2);
  visibility: ${(props) => (props.$visibility ? 'visible' : 'hidden')};
  &:active {
    color: var(--navy-blue-1);
  }
`;
export default function GuidePage() {
  const [activeSlide, setActiveSlide] = useState(0);
  const [swiper, setSwiper] = useState<SwiperClass>();

  return (
    <Section>
      <MainWrapper>
        <Swiper
          onSwiper={(swiper) => setSwiper(swiper)}
          onRealIndexChange={(element) => setActiveSlide(element.activeIndex)}
          pagination={{
            dynamicBullets: true,
          }}
          modules={[Pagination]}
          className="mySwiper"
        >
          <GuideSwiperSlide>
            <img src={guidePic1} alt="" />
          </GuideSwiperSlide>
          <GuideSwiperSlide>
            <img src={guidePic2} alt="" />
          </GuideSwiperSlide>
        </Swiper>
        <Title>
          {activeSlide === 0 ? 'Управляйте подписками' : 'Все в одном месте'}
        </Title>
        <SubTitle>
          {activeSlide === 0
            ? 'Представлены все ваши подписки, которыми можно управлять'
            : 'Можно развернуть меню с календарем, вашими подписками, платежами и FAQ'}
        </SubTitle>
      </MainWrapper>
      <LinkWrapper>
        {activeSlide === 0 ? (
          <Button onClick={() => swiper?.slideNext()} variant="contained">
            Далее
          </Button>
        ) : (
          <Button component={Link} to={'/'} variant="contained">
            Здорово
          </Button>
        )}

        <OnbordingLink $visibility={activeSlide === 0 ? true : false} to={'/'}>
          Перейти на главный экран
        </OnbordingLink>
      </LinkWrapper>
    </Section>
  );
}
